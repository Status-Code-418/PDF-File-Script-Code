from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject, create_string_object

input_pdf = "example.pdf"   # alert 액션을 추가할 PDF 파일 경로
output_pdf = "alert_pdf.pdf"    # 자바스크립트 액션이 추가된 PDF 파일 경로

reader = PdfReader(input_pdf)
writer = PdfWriter()

# 모든 페이지 복사
for page in reader.pages:
    writer.add_page(page)

# 자바스크립트 액션 생성
js_dict = DictionaryObject()
js_dict.update({
    NameObject("/S"): NameObject("/JavaScript"),
    NameObject("/JS"): create_string_object("app.alert('PDF 파일이 열렸습니다!');")
    # 위의 자바스크립트 코드는 PDF 파일이 열릴 때 alert 창을 띄우는 예시입니다. 필요에 따라 다른 자바스크립트 코드를 사용할 수 있습니다.
})

writer._root_object.update({
    NameObject("/OpenAction"): js_dict
})

with open(output_pdf, "wb") as f_out:
    writer.write(f_out)

print(f"{output_pdf} 생성 완료")