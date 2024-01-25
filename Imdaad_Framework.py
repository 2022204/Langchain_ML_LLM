

Evaluated_Parameters = {"Parameter_1": 0,"Parameter_2": 0,"Parameter_3": 0,"Parameter_4": 0,"Parameter_5": 0,"Parameter_6": 0,
            "Parameter_7": 0,"Parameter_8": 0,"Parameter_9": 0,"Parameter_10": 0,"Parameter_11": 0, "Parameter_12": 0,
            "Parameter_13": 0,"Parameter_14": 0,"Parameter_15": 0}

focused_characters = ["Parameter_1","Parameter_2","Parameter_3","Parameter_4","Parameter_5","Parameter_6",
                      "Parameter_7","Parameter_8","Parameter_9","Parameter_10","Parameter_11", "Parameter_12",
                      "Parameter_13","Parameter_14","Parameter_15"]

def validate():
    """Response Validation"""



def evaluated_response(prompt):
    """Response evaluation"""


def questionaire():
    """User enters the question/Answer session"""

    with open("Questions.txt","r") as file:
        i = 0
        for line in file:
            while True:
                response = input(line.strip())

                if not validate(response): 
                    print("TRY AGAIN. You couldn't Answer the question correctly.")

                break
            
            Evaluated_Parameters[focused_characters[i]] = evaluated_response(response)
            
            i += 1


def classify():
    """Classification using Evaluated Parameters"""
    #return model.output(Evaluated_Parameters)

def print():
    for i in Evaluated_Parameters:
        print(i, Evaluated_Parameters[i])

def therapy(Classified_Type):
    """This will find the appropriate therapy for the Patient"""

    #return Therapy
def main():
    questionaire()

    Classified_Type = classify()


    print(therapy(Classified_Type))    



if __name__ == "__main__":
    main()