# Class Scheduler

This program can help turn a list of classes you're interested in into a list of conflict-free class schedules. 

## Data

The first step is to make a list of classes and conflicts, formatted like this:
  
    Classes:
    Classname | Class Code | Class Tag | Class Rating
    # Classname | Class Code | Class Tag | Class Rating
    ...
    ...
    Classname | Class Code | Class Tag | Class Rating
    Conflicts:
    Class Code - Class Code
    ...
    ...
    Class Code - Class Code - Class Code - Class Code
    Class Code - Class Code
    Class Code - Class Code - Class Code
    Class Code - Class Code

Where classname can be anything that you'd like to refer to the class as (AI, Algo, etc). The classcode is a unique code assigned to the class, so you might want to use something like: MATH 2230. The class tag is for identifying types of classes, according to your personal scheduling needs, like: Biology_Core, Music, Tech_Elective, etc. The class rating is a number (that should probably be less than 1) that expresses your preference for the class (higher is better). Classes with a ```#``` before them will be ignored (this is good for adapting to classes filling up). 

The conflict list contains pairs or arbitrary tuples of classes, identified by their class code, that conflict. In other words, no schedule will be suggested with two classes that appear on the same conflict line.

This data should be stored in a text file. 

## Usage

Then, run the scheduler script like this:

    python3 schedule.py filename num_classes minimal_rating critical_tags single_tags
    
Where:

```filename``` is the name of the file containing the class, confict, and preference information above

```num_classes``` is the number of classes you want in your schedule

```minimal_rating``` is the minimum schedule rating you want to consider

```critical_tags``` is a list of tags (like ["tag1", "tag3"]) that you really want to be included in your schedule (you might want to require one core class, or one distribution requirement class)

```single_tags``` is a list of tags that you don't want to occur more than once in your schedule (you can leave it off, and it will be the same as ```critical_tags```)

If you are comfotable doing so, you might consider changing the default values in your local copy of the python code to avoid adding all these command line parameters. 

The rating of a schedule is computed by summing all of the ratings of the constituent classes, plus 1 for each of the critical tags that are present (this is why your ratings should be less than 1). 

The output will be a printed list of acceptable schedules, sorted with the best at the bottom, and each labeled with their rating. 

## Extension

Possible improvements include:
* adding consideration for number of credits
* adding different class options, like different lecture/discussion section times
* speeding up the algorithm (it currently takes several seconds to run with 17 classes considered)
