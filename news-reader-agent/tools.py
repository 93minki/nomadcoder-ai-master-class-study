# tool 함수를 만들 때 doc string을 작성해서 CrewAI 한테 이 툴에 대한 설명을 전달할 수 있음(함수의 스키마)


from crewai.tools import tool


@tool

def count_letters(sentence: str):
    """
    This function is to count the amount of letters in a sentence.
    The input is a `sentence` string.
    The output is a number.
    """
    print("tool called with input:", sentence)
    return len(sentence)