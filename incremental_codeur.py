import RPi.GPIO as GPIO
CODER_SW = 11
CODER_CW_DT = 13
CODER_CCW_CLK = 15
def codersetup():
    GPIO.setup(CODER_SW, GPIO.IN)
    GPIO.setup(CODER_CW_DT, GPIO.IN)
    GPIO.setup(CODER_CCW_CLK, GPIO.IN)

def coder():
    status = 0
    previousStateCLK = 0
    previousStateDT = 0
    while (status == 0):
        CLKstate = GPIO.intput(CODER_CW_DT)
        DTstate = GPIO.intput(CODER_CW_DT)
        if(GPIO.intput(CODER_SW) == True):
            status = 1
            return(status)
        elif(CLK == 0 and DT == 0):
            if(previousStateDT == 0 and previousStateCLK == 1):
                status = 3
                return(status)
            if(previousStateDT == 0 and previousStateCLK == 1):
                status = 2
                return(status)
        previousStateCLK = CLKstate
        previousStateDT = DTstate
        