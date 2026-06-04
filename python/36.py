def find_common_skills(skills1, skills2):
    if not isinstance(skills1, set) or not isinstance(skills2, set):
        print("Inputs must be sets")
        return
    common = skills1 & skills2
    print(f"Common Skills: {common}")

set1 = {"Python", "SQL", "Java"}
set2 = {"Python", "C++", "AWS"}
find_common_skills(set1, set2)
