#imports and global vars
import time
#add_library('sound')
arr = [1]
start_time = time.time()
lines = [0]
obj = False
current_note = 2
curr_timing = 0
circles = [0]
arrpos = 0
timing = [0]
lane = [1]
arrTiming = [0] 
y = 0
click_y = 0
score = 0
gameplay = False

#read a 4k mania .osu file and output the millisecond time of the objects and what lane they are in
def parse_osu_file(osu_file):
    global arr, start_time, lines, obj, arrTiming
    #open file
    with(open(osu_file, 'r')) as f:
        lines = list(f)
        i = 0
        #process lines
        for lines in lines:
            #lines in a text file have newline markers at the end, this gets rid of them
            Line = lines.strip('\n')
            #split on comma to extract the info needed
            data = Line.split(',')
            #info from file
            x = data[0]
            x = int(x)
            timing = data[2]
            timing = int(timing)

            #calculate which lane to output
            if(x == 64):
                arr.append(1)
            elif(x == 192):
                arr.append(2)
            elif(x == 320):
                arr.append(3)
            elif(x == 448):
                arr.append(4)
            #very basic error handling
            else: 
                print("Error on line " + str(i))
                break
            #legacy timing
            arrTiming.append(timing)
            i += 1
    return arr, arrTiming
#parse .osu file for level
arr, arrTiming = parse_osu_file(r"C:\Users\bodie\OneDrive\Desktop\py\maniaknockoff\xi - ANiMA (Kuo Kyoka) [Kyou's 4K Lv.9].osu")
end_time = time.time()
#Print Debug info to console
print("=========DEBUG=========")
print("file len: " + str(len(lines)))
print("object count: " + str(len(arr)))
print("Time to parse file: " + str((end_time - start_time)*1000) + "ms")
print("=======END DEBUG=======")

#setup
def setup():
    #screen size
    size(750,750)
    #limit FPS
    frameRate(144)
    #color stuff
    fill(255,255,255)
    stroke(255,255,255)


    
#check what lane is pressed
def keyPressed():
    global curr_timing, current_note, y, click_y, score, gameplay
    if key == 'n' or key == 'N':
        gameplay = True
    if 's' in key:
        circle(125+50,700,100)
        #fail player if they press wrong key
        if arr[current_note+1] != 1:
            score = score - 300
        else:
            #legacy timing
            curr_timing = ((time.time() - start_time) - end_time)*1000
            #load next note in sequence
            current_note = current_note + 1
            #scoring based on timing
            click_y = y
            score = score + ((750 - click_y)/5)
            y = 0
        
    if 'd' in key:
        circle(250+50,700,100)
        if arr[current_note+1] != 2:
            score = score - 300
        else:
            curr_timing = ((time.time() - start_time) - end_time)*1000
            current_note = current_note + 1
            click_y = y
            score = score + ((750 - click_y)/5)
            y = 0
    if 'l' in key:
        circle(375+50,700,100)
        if arr[current_note+1] != 3:
            score = score - 300
        else:
            curr_timing = ((time.time() - start_time) - end_time)*1000
            current_note = current_note + 1
            click_y = y
            score = score + ((750 - click_y)/5)
            y = 0
    if ';' in key:
        circle(500+50,700,100)
        if arr[current_note+1] != 4:
            score = score - 300
        else:
            curr_timing = ((time.time() - start_time) - end_time)*1000
            current_note = current_note + 1
            click_y = y
            score = score + ((750 - click_y)/5)
            y = 0
def draw():
    global current_note, curr_timing, circles, start_time, timing, lane, y,score,gameplay
    background(0)
    #judgement line
    line(125,650,625,650)
    
    #gameplay screen
    if gameplay == True:
        #legacy timing stuff
        frame_time = time.time()*1000

        #spawn circle in correct lane based off of the value in arr
        circle(arr[current_note+1]*1500/12+50,y,65)
        y = y + 10
        
        
        #display score
        textSize(24)
        text(str(score),20, 50)
        
        #win screen
        if current_note == len(arr):
            textSize(48)
            text("Congrats" + '\n' + "score: " + str(score), 135, 375)
            
        #lose screen    
        if y > 750:
            gameplay = False
        if score < 0:
            gameplay = False
    #start menu
    else:
        textSize(48)
        text("Press N To Start!", 135, 375)
        y = 0
        current_note = 2
        score = 0
        
