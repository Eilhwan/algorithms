class Student:
    def __init__(self, name):
        self.name = name
        self.korean = 100
        self.english = 100
        print("객체가 생성되었습니다.")
    
    def get_sum(self):
        return self.korean + self.english



print(Student("전일환").get_sum())