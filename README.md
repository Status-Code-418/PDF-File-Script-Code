# PDF File Script Collection

이 저장소는 `pypdf` 라이브러리를 활용하여 PDF 파일에 보안 기능을 추가하거나 특정 동작을 수행하도록 수정하는 Python 스크립트 모음입니다.

## 포함된 스크립트

### 1. PDF 암호 설정 (`PDF Script Code(Open Password).py`)
이 스크립트는 기존 PDF 파일에 비밀번호를 설정하여 권한이 없는 사용자가 파일을 열어보는 것을 방지합니다.
- **기능**: 사용자(User) 및 소유자(Owner) 비밀번호 설정, 128비트 암호화 적용.
- **출력**: 암호화된 새로운 PDF 파일 생성.

### 2. PDF 오픈 액션 리다이렉트 (`PDF Script Code(OpenAction Redirect).py`)
이 스크립트는 PDF 파일이 열릴 때 특정 웹사이트로 자동 리다이렉트되는 JavaScript 액션을 추가합니다.
- **기능**: PDF의 루트 오브젝트에 `/OpenAction`을 추가하여 파일 오픈 시 `app.launchURL` 실행.
- **참고**: 보안상의 이유로 Adobe Reader 9.2 이하 버전 등 일부 구형 뷰어에서만 동작하며, 최신 뷰어에서는 실행이 차단될 수 있습니다.

### 3. PDF 단순 경고창 출력 (`PDF Script Code(Alert).py`)
이 스크립트는 PDF 파일을 열 때 사용자에게 간단한 알림 메시지를 표시합니다.
- **기능**: `/OpenAction`을 통해 `app.alert` 자바스크립트를 실행하여 팝업 메시지를 출력합니다.

### 4. PDF 뷰어 정보 출력 (`PDF Script Code(Viewer Information Alert).py`)
이 스크립트는 PDF를 열고 있는 프로그램(뷰어)의 이름과 버전 정보를 경고창으로 보여줍니다.
- **기능**: `app.viewerType`과 `app.viewerVersion` 변수를 활용하여 환경 정보를 확인합니다.
- **용도**: 특정 뷰어에서의 호환성 테스트나 환경 확인 용도로 사용됩니다.

### 5. PDF 뷰어 버전 체크 및 경고 (`PDF Script Code(Viewer Version Check Alert).py`)
이 스크립트는 사용자의 PDF 뷰어 버전을 검사하여 특정 조건(Adobe Reader 9.x)이 아닐 경우 호환성 경고 메시지를 표시합니다.
- **기능**: JavaScript 로직을 통해 뷰어 이름과 버전을 체크하고, 조건에 맞지 않으면 `app.alert`를 실행합니다.
- **특징**: `TextStringObject`를 사용하여 복잡한 멀티라인 자바스크립트 코드를 삽입합니다.

## 요구 사항

스크립트를 실행하기 위해서는 Python 3.x 환경과 `pypdf` 라이브러리가 필요합니다.

```bash
pip install pypdf
```

## 사용 방법

1. **준비**: 수정하려는 원본 PDF 파일(`example.pdf`)을 스크립트와 같은 폴더에 배치합니다.
2. **설정**: 각 스크립트 상단의 `input_pdf`, `output_pdf`, `password` 또는 `target_url` 변수를 목적에 맞게 수정합니다.
3. **실행**:
   ```bash
   python "PDF Script Code(Open Password).py"
   # 또는
   python "PDF Script Code(OpenAction Redirect).py"
   # 또는
   python "PDF Script Code(Alert).py"
   # 또는
   python "PDF Script Code(Viewer Information Alert).py"
   # 또는
   python "PDF Script Code(Viewer Version Check Alert).py"
   ```

## 주의 사항

- **보안**: JavaScript 리다이렉트 기능은 최신 웹 브라우저 내장 PDF 뷰어나 보안이 강화된 최신 PDF 리더기에서는 작동하지 않을 수 있습니다.
- **라이브러리**: 기존 `PyPDF2` 라이브러리의 최신 버전인 `pypdf`를 사용하므로, 구버전 설치 시 오류가 발생할 수 있습니다. 반드시 `pip install pypdf`를 통해 설치하세요.
- **법적 책임**: 이 스크립트를 사용하여 생성된 결과물에 대한 책임은 사용자 본인에게 있습니다.