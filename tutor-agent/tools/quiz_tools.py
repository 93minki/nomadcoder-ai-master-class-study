from typing import Literal

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class Question(BaseModel):
    question: str = Field(description="The quiz question text")
    options: list[str] = Field(
        description="Exactly 4 multiple choice options, labeled A, B, C, and D."
    )
    correct_answer: str = Field(
        description="The correct answer (MUST MATCH ONE OF 'options')"
    )
    explanation: str = Field(
        description="Explanation of why the answer is correct and the other ones are wrong."
    )


class Quiz(BaseModel):
    topic: str = Field(description="The main topic being tested")
    questions: list[Question] = Field(description="List of the quiz questions")


@tool
def generate_quiz(
    research_text: str,
    topic: str,
    difficulty: Literal[
        "easy",
        "medium",
        "hard",
    ],
    num_questions: int,
):
    """
    연구 정보를 바탕으로 객관식 문제로 구성된 구조화된 퀴즈를 생성합니다.
    Args:
        research_text: str - 주제에 관한 연구 정보입니다. 다음과 같은 형태일 수 있습니다:
                      - 웹 검색에서 얻은 원문
                      - 연구 결과 요약
                      - 주제와 관련된 모든 정보
                      - 비어 있으면 일반 지식을 바탕으로 문제를 생성합니다
        topic: str - 퀴즈의 주요 주제/과목입니다(예: "Python 프로그래밍", "제2차 세계 대전", "광합성")
        difficulty: Literal["easy", "medium", "hard"] - 난이도입니다:
                   - "easy": 기본 개념, 정의, 간단한 사실
                   - "medium": 개념의 적용, 아이디어 간의 연관성
                   - "hard": 복잡한 분석, 종합, 고급 이해
        num_questions: int - 생성할 문제의 수입니다(1~30)
                      일반적인 값: 3~5(짧은 퀴즈), 6~10(중간 길이), 11~15(긴 퀴즈)
    Returns:
        다음 항목을 포함하는 구조화된 문제들로 구성된 Quiz 객체:
        - question: 문제 내용
        - options: 4개의 객관식 답변 목록
        - correct_answer: 정답(보기 중 하나와 정확히 일치해야 함)
        - explanation: 정답에 대한 자세한 설명
    Example usage:
        research_info = "머신 러닝은 알고리즘에 중점을 둔 AI의 한 분야입니다..."
        quiz = generate_quiz(research_info, "Machine Learning", "medium", 5)
    """
    model = init_chat_model(model="openai:gpt-4o")
    structured_model = model.with_structured_output(Quiz)

    prompt = f"""
        Create a {difficulty} quiz, about {topic} with {num_questions} using the following research information.

        <RESEARCH_INFORMATION>
        {research_text}
        </RESEARCH_INFORMATION>

        Make sure to use the RESEARCH_INFORMATION to create the most accurate questions.
    """

    quiz = structured_model.invoke(prompt)

    return quiz
