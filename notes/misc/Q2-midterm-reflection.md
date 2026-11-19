Objective: explain **briefly** how I solved each question and if I got i wrong explain in **depth** why i got it wrong and how to improve.
<hr>

## Question 1:
```
A company that develops educational software wants to assemble a collaborative team of developers from a variety of professional and cultural backgrounds. Which of the following is NOT considered a benefit of assembling such a team?

A) Collaboration that includes diverse backgrounds and perspectives can eliminate the need for software testing.

B) Collaboration that includes diverse backgrounds and perspectives can help the team anticipate the needs of a variety of software users.

C) Collaboration that includes diverse backgrounds and perspectives can help the team avoid bias.

D) Collaboration that includes diverse backgrounds and perspectives can reflect the strengths of the individual team members.
```
**my answer:** `A` <br>
**correct answer:** `A`<br>
**Rationale:**
```
I picked A since the question explicitly states which of the following is NOT considered a benefit.

A states that collaborations completetly eliminate software-testing, which is majorly note true as
logic errors can happen, even with a very diverse group of programmers. Therefore, A is most likely the answer.

B states that collaborations can help manage users, which is false-ish? but it is so indirect it should not be 
the answer.

C states that collaborations can help teams avoid bias in code, which is true as collaborations can prevent
software blind spots from forming or make the team make sharper decisions. However, we are NOT looking for
a benefit; this describes a benefit, therefore, C is not the answer.

D states that collaboration can reflect the strengths of individuals, which is true as having a variety of backgrounds represented on a team can result in the team to make use of the different advantages of individual team members. As a result, D is likely not the answer

leaving A as the only viable option.
```

<hr>

## Question 2:
```
A student is creating an application that allows customers to order food for delivery from a local restaurant. Which of the following is LEAST likely to be an input provided by a customer using the application?

A) The address where the order should be delivered

B) The cost of a food item currently available for order

C) The credit card or payment information for the purchaser

D) The name of a food item to be included in the delivery
```
**my answer:** `B` <br>
**correct answer:** `B`<br>
**Rationale:**
```
I picked B since it is the only one among the answer choices that makes intuitive sense:
A talks about the user inputting the address where the order should be delivered which is required to engage
in online delivery, making A not the answer; C talks about the user inputting the credit card for payment, 
which is once again required, making C not the answer; and D talks about the user inputting the name of the 
food item for delivery, which is—like the others—a required element for online delivery.

Therefore leaving B as the only viable option.
```

<hr>

## Question 3:
```
In the following code segment, `score` and `penalty` are initially positive integers.
The code segment is intended to reduce the value of `score` by `penalty`.
However, if doing so would cause `score` to be negative, `score` should be assigned the value `0`.

For example, if `score` is `20` and `penalty` is `5`, the code segment should set `score` to `15`.
If `score` is `20` and `penalty` is `30`, `score` should be set to `0`.

The code segment does not work as intended.

Line 1: IF (score - penalty < 0)
Line 2: {
Line 3:    score ← score - penalty
Line 4: }
Line 5: ELSE
Line 6: {
Line 7:    score ← 0
Line 8: }

Which of the following changes can be made so that the code segment works as intended?

A) Changing line 1 to IF(score < 0)

B) Changing line 1 to IF(score + penalty < 0)

C) Changing line 7 to score ← score + penalty

D) Interchanging lines 3 and 7
```
**my answer:** `D` <br>
**correct answer:** `D`<br>
**Rationale:**
```
I picked D as a result of executing test-case scenarios: the given test case, score = 20 and penalty = 5, 
can be used to diagnose the bug within the code. Following the code, if score = 20, the first if block should
be false since 20-5 = 15 ≮ 0. The else codeblock then sets the score to 0. I can see that when (score - penalty)
was greater than 0, it set score to 0; else, if (score - penalty) is less than 0, it get score to (score - penalty).
This means that the logic for these two codeblocks was switched around. suggesting that interchanging
lines 3 and 7 should fix the code.

Therefore leaving D as the only viable option.
```

<hr>

## Question 4:
```
The following procedure is intended to return `true` if the list of numbers `myList` contains only positive 
numbers and is intended to return `false` otherwise. The procedure does not work as intended.

```text
PROCEDURE allPositive(myList)
{
    index ← 1
    len ← LENGTH(myList)
    REPEAT len TIMES
    {
        IF (myList[index] > 0)
        {
            RETURN(true)
        }
        index ← index + 1
    }
    RETURN(false)
}

For which of the following contents of myList does the procedure NOT return the intended result?

A) [-3, -2, -1]

B) [-2, -1, 0]

C) [-1, 0, 1]

D) [1, 2, 3]
```
**my answer:** `C` <br>
**correct answer:** `C`<br>
**Rationale:**
```
Similarly to Question 3, I solved this question using test cases (in this context, from the lists). 
The question wants a test case where the code does NOT work. To do that, I had to try every list to see
which one broke the code.

test case A) everything here is negative numbers, therefore, processing it through the procedure would make the he procedure then returns false as intended.
```

## Question 5:
```
A computer program uses 3 bits to represent integers. When the program adds the decimal
(base 10) numbers 5 and 3, the result is 0. Which of the following is the best explanation
for the result?

A) An overflow error occurred.

B) round-off error occurred.

C) The result was affected by lossy data compression.

D) The result was approximated by a floating-point representation.
```
**my answer:** `A` <br>
**correct answer:** `A`<br>
**Rationale:**
```
I mainly solved this question by using my knowledge of binary and decimal: 3 bits can store at MAX 8 in decimal.
Therefore, for any integer k where k > 8, it would cause a overflow error to occur in the domain of 3 bits.

Therefore leaving A as the only viable option.
```

## Question 6:
```
A binary number is to be transformed by appending three 0s to the end of the number.
For example, 11101 is transformed to 11101000.

Which of the following correctly describes the relationship between the transformed
number and the original number?

A) The transformed number is 3 times the value of the original number.

B) The transformed number is 4 times the value of the original number.

C) The transformed number is 8 times the value of the original number.

D)The transformed number is 1,000 times the value of the original number.
```
**my answer:** `C` <br>
**correct answer:** `C`<br>
**Rationale:**
```
Similarlly to Question 5, i used my knowledge of binary and decimal to know that when
a zero is appended to a binary number, it multiplys the binary value by a factor of 2^n
where n is the number of zeros appended.

In this case, since theres 3 zeros appended, it will be multiplied by 2^3, which is 8

Therefore leaving C as the only viable option.
```

## Question 7:
```
A video game character can face toward one of four directions: north, south, east, and west.
Each direction is stored in memory as a sequence of four bits. A new version of the game is
created in which the character can face toward one of eight directions, adding northwest,
northeast, southwest, and southeast to the original four possibilities.
Which of the following statements is true about how the eight directions must be stored in memory?

A) Four bits are not enough to store the eight directions. Five bits are needed for the new version of the game.

B) Four bits are not enough to store the eight directions. Eight bits are needed for the new version of the game.

C) Four bits are not enough to store the eight directions. Sixteen bits are needed for the new version of the game.

D) Four bits are enough to store the eight directions.
```
**my answer:** `B` <br>
**correct answer:** `D`<br>
**Rationale:**
```
Similarlly to Question 5, i used my knowledge of binary and decimal to know that when
a zero is appended to a binary number, it multiplys the binary value by a factor of 2^n
where n is the number of zeros appended.

In this case, since theres 3 zeros appended, it will be multiplied by 2^3, which is 8

Therefore leaving C as the only viable option.
```