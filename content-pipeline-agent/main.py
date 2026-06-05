from crewai.flow.flow import Flow, listen, start, router, and_, or_
from pydantic import BaseModel


class MyFirstFlowState(BaseModel):
    user_id: int = 1
    is_admin: bool = False


class MyFirstFlow(Flow[MyFirstFlowState]):

    @start()
    def first(self):
        print(self.state.user_id)
        print("hello")

    @listen(first)
    def second(self):
        self.state.user_id = 2
        print("world")

    @listen(first)
    def third(self):
        print("!")

    @listen(and_(second, third))
    def final(self):
        print(":)")

    @router(final)
    def route(self):
        if self.state.is_admin:
            return "even!"  # "even" 이라는 이름의 이벤트를 발생한다.
        else:
            return "odd"

    @listen(
        "even"
    )  # @listen은 메서드 뿐만아니라 "even" 이라는 이름의 이벤트를 받을 수 있다.
    def handle_even(self):
        print("even")

    @listen("odd")
    def handle_odd(self):
        print("odd")


flow = MyFirstFlow()

# flow.plot()
flow.kickoff()
