import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

st.title("나만의 챗GPT 테스트")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 사이드바 생성
with st.sidebar:
    # 대화 초기화 버튼 생성
    clear_button = st.button("대화 초기화")


def print_messages():
    for chat_message in st.session_state.messages:
        st.chat_message(chat_message.role).write(chat_message.content)


# 이전 대화 기록을 저장한다.
def add_message(role, message):
    st.session_state.messages.append(ChatMessage(role=role, content=message))


# chain 생성
def create_chain():
    # prompt | llm | output_parser
    prompt = ChatPromptTemplate.from_messages(
        [("system", "You are a helpful assistant."), ("user", "#QuestionL\n{question}")]
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain


if clear_button:
    st.session_state.messages = []
print_messages()

# 사용자의 입력
user_input = st.chat_input("궁금한 내용을 물어보세요.")
if user_input:  # 만약에 사용자 입력이 들어오면...
    # st.write(f"사용자 입력: {user_input}")
    # 사용자 입력을 표시한다.
    with st.chat_message("user"):
        st.write(user_input)
    # chain 생성
    chain = create_chain()
    response = chain.stream({"question": user_input})
    with st.chat_message("assistant"):
        # 빈 공간(컨테이너)을 만들어서, 여기에 토큰을 스트리밍 출력한다.
        container = st.empty()
        AI_answer = ""
        for token in response:
            AI_answer += token
            container.markdown(AI_answer)
    # AI_answer = chain.invoke({"question": user_input})
    # st.chat_message("assistant").write(AI_answer)

    # 대화 기록을 저장한다.
    add_message("user", user_input)
    add_message("assistant", AI_answer)
