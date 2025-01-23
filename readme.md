# 나만의 챗GPT 애플리케이션

이 프로젝트는 Streamlit과 LangChain을 활용하여 만든 간단한 챗봇 애플리케이션입니다.

## 주요 기능

- OpenAI의 GPT-4를 활용한 대화형 인터페이스
- 실시간 스트리밍 응답
- 대화 기록 저장 및 표시
- 대화 초기화 기능

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install streamlit langchain-core langchain-openai python-dotenv
```

2. `.env` 파일 설정:
프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 내용을 입력하세요:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## 실행 방법

다음 명령어로 애플리케이션을 실행합니다:
```bash
streamlit run main.py
```

## 사용 방법

1. 브라우저에서 애플리케이션이 실행되면 하단의 입력창에 질문을 입력합니다.
2. AI 어시스턴트가 실시간으로 응답을 생성합니다.
3. 대화 내용은 자동으로 저장되며, 사이드바의 '대화 초기화' 버튼으로 초기화할 수 있습니다.

## 프로젝트 구조

```
MyProject/
├── main.py              # 메인 애플리케이션 파일
├── README.md           # 프로젝트 문서
└── .env                # 환경 변수 설정 파일
```

## 주요 코드 설명

- `main.py`: Streamlit 웹 인터페이스와 LangChain을 통한 AI 대화 로직 구현
- 대화 기록은 Streamlit의 session_state를 통해 관리됨
- LangChain의 ChatOpenAI와 ChatPromptTemplate을 활용한 AI 응답 생성
- 실시간 스트리밍을 위한 StrOutputParser 활용

## 라이선스

이 프로젝트는 MIT 라이선스 하에 공개되어 있습니다.
```

이 README 파일은 프로젝트의 기본적인 정보, 설치 방법, 사용 방법, 프로젝트 구조 등을 포함하고 있습니다. 필요에 따라 내용을 수정하거나 추가하실 수 있습니다.
