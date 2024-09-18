class Student:
    def __init__(self, name, roll_number, grades):
        self.name = name
        self.roll_number = roll_number
        self.grades = grades  

    def calculate_average(self):
        total = sum(self.grades.values())
        num_subjects = len(self.grades)
        return total / num_subjects

    def get_highest_score(self):
        return max(self.grades.values())

    def get_lowest_score(self):
        return min(self.grades.values())

    def get_grade_distribution(self):
        distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for score in self.grades.values():
            if 90 <= score <= 100:
                distribution["A"] += 1
            elif 80 <= score < 90:
                distribution["B"] += 1
            elif 70 <= score < 80:
                distribution["C"] += 1
            elif 60 <= score < 70:
                distribution["D"] += 1
            else:
                distribution["F"] += 1
        return distribution


class ProgressReport:
    def __init__(self, student, assessments, scores):
        self.student = student
        self.assessments = assessments  
        self.scores = scores  

    def calculate_progress(self):
        total_score = 0
        for assessment in self.assessments:
            subject_scores = self.scores.get(assessment, {})
            total_score += sum(subject_scores.values())
        return total_score / len(self.assessments)

    def get_improvement_rate(self):
        improvement_report = {}
        
        for i in range(1, len(self.assessments)):
            previous_scores = self.scores[self.assessments[i - 1]]  
            current_scores = self.scores[self.assessments[i]]       

            previous_total = sum(previous_scores.values())
            current_total = sum(current_scores.values())

            if current_total > previous_total:
                result = "improved"
            elif current_total < previous_total:
                result = "declined"
            else:
                result = "stayed the same"

            improvement_report[self.assessments[i]] = result
        
        return improvement_report

    def get_subject_progress(self, subject):
        subject_scores = []
        for assessment in self.assessments:
            subject_scores.append(self.scores.get(assessment, {}).get(subject, 0))
        return subject_scores


class DataAnalysis:
    def __init__(self, students):
        self.students = students

    def average_grade(self):
        total_average = 0
        for student in self.students:
            total_average += student.calculate_average()
        return total_average / len(self.students)

    def highest_and_lowest_grades(self):
        highest = {}
        lowest = {}
        for student in self.students:
            highest[student.name] = student.get_highest_score()
            lowest[student.name] = student.get_lowest_score()
        return highest, lowest

    def grade_distribution(self):
        overall_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for student in self.students:
            distribution = student.get_grade_distribution()
            for grade, count in distribution.items():
                overall_distribution[grade] += count
        return overall_distribution

    def failing_students(self, passing_grade=60):
        failing_students = []
        for student in self.students:
            if student.get_lowest_score() < passing_grade:
                failing_students.append(student.name)
        return failing_students

    def top_performers(self, top_n=3):
        averages = {student.name: student.calculate_average() for student in self.students}
        sorted_averages = sorted(averages.items(), key=lambda item: item[1], reverse=True)
        return sorted_averages[:top_n]

    def subject_wise_analysis(self, subject):
        subject_grades = {student.name: student.grades.get(subject, 0) for student in self.students}
        return subject_grades

    def student_improvement(self, progress_reports):
        for report in progress_reports:
            improvement = report.get_improvement_rate()

            print(f"\nStudent: {report.student.name}")
            for assessment, result in improvement.items():
                print(f"From {report.assessments[0]} to {assessment}, the student's performance has {result}")

    def class_performance(self, historical_average):
        current_average = self.average_grade()
        difference = current_average - historical_average
        return {
            "current_average": current_average,
            "historical_average": historical_average,
            "difference": difference
        }

    @staticmethod
    def save_students_to_file(students, filename="students_data.txt"):
        with open(filename, "w") as file:
            for student in students:
                grades_str = ",".join([f"{subject}:{score}" for subject, score in student.grades.items()])
                file.write(f"{student.name},{student.roll_number},{grades_str}\n")

    @staticmethod
    def load_students_from_file(filename="students_data.txt"):
        students = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    name = data[0]
                    roll_number = int(data[1])
                    grades = {subject_score.split(":")[0]: int(subject_score.split(":")[1]) for subject_score in data[2:]}
                    students.append(Student(name, roll_number, grades))
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return students


# Load students from file if available
students = DataAnalysis.load_students_from_file()
if not students:  # If no file is found, use default students
    students = [
        Student("Aniket", 1, {"Math": 85, "Science": 92, "English": 78}),
        Student("Baali", 2, {"Math": 71, "Science": 49, "English": 60}),
        Student("Amit", 3, {"Math": 85, "Science": 85, "English": 81}),
        Student("Rajesh", 4, {"Math": 45, "Science": 80, "English": 60}),
        Student("Priya", 5, {"Math": 92, "Science": 71, "English": 89}),
        Student("Sunil", 7, {"Math": 78, "Science": 70, "English": 55}),
        Student("Rohit", 8, {"Math": 82, "Science": 89, "English": 90}),
        Student("Anjali", 6, {"Math": 67, "Science": 73, "English": 80}),
        Student("Neha", 9, {"Math": 95, "Science": 94, "English": 93}),
        Student("Sneha", 10, {"Math": 66, "Science": 61, "English": 72}),
        Student("Vikas", 11, {"Math": 85, "Science": 87, "English": 79}),
        Student("Kavita", 12, {"Math": 61, "Science": 49, "English": 88}),
        Student("Arjun", 13, {"Math": 78, "Science": 75, "English": 80}),
        Student("Pooja", 14, {"Math": 75, "Science": 55, "English": 82}),
        Student("Nikhil", 15, {"Math": 75, "Science": 40, "English": 68}),
        Student("Karan", 16, {"Math": 80, "Science": 67, "English": 52}),
        Student("Rahul", 17, {"Math": 50, "Science": 43, "English": 95}),
        Student("Suman", 18, {"Math": 63, "Science": 55, "English": 84}),
        Student("Shweta", 19, {"Math": 88, "Science": 40, "English": 60}),
        Student("Manish", 20, {"Math": 78, "Science": 72, "English": 80}),
        Student("Ravi", 21, {"Math": 62, "Science": 55, "English": 71}),
    ]

# Initialize the analysis after loading or creating students
analysis = DataAnalysis(students)

def menu():
    global analysis  # Declare analysis as a global variable
    while True:
        print("\nMenu:")
        print("1. Calculate Class Average Grade")
        print("2. Get Top Performers")
        print("3. Get Grade Distribution")
        print("4. Get Failing Students")
        print("5. Get Student Improvement")
        print("6. Save Students to File")
        print("7. Load Students from File")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            average_grade = analysis.average_grade()
            print(f"Average grade of the class: {average_grade}")

        elif choice == 2:
            top_students = analysis.top_performers()
            print("Top performers:", top_students)

        elif choice == 3:
            grade_distribution = analysis.grade_distribution()
            print("Grade distribution:", grade_distribution)

        elif choice == 4:
            failing_students = analysis.failing_students()
            print("Failing students:", failing_students)

        elif choice == 5:
            analysis.student_improvement(progress_reports)

        elif choice == 6:
            DataAnalysis.save_students_to_file(students)
            print("Student data saved to file.")

        elif choice == 7:
            loaded_students = DataAnalysis.load_students_from_file()
            analysis = DataAnalysis(loaded_students)
            print("Student data loaded from file.")

        elif choice == 8:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select a valid option.")
        
        continue_choice = int(input("\nTo continue, press 1. To exit, press 0: "))
        if continue_choice == 0:
            print("Exiting the program.")
            break

# Creating sample progress reports
progress_reports = [
    ProgressReport(Student("Aniket", 1, {"Math": 85, "Science": 92}), ["Test 1", "Test 2"], {"Test 1": {"Math": 80, "Science": 90}, "Test 2": {"Math": 85, "Science": 92}}),
    ProgressReport(Student("Baali", 2, {"Math": 71, "Science": 49}), ["Test 1", "Test 2"], {"Test 1": {"Math": 85, "Science": 78}, "Test 2": {"Math": 88, "Science": 79}}),
]

# Start the menu
menu()
