import re

def arithmetic_arranger(problems, *solve):

    # input tests
    inputTest = True
    while inputTest:
      if len(problems) > 5:
          return "Error: Too many problems."
          inputTest = False
      for problem in problems:
        newProblemTest = problem.split()
        firstIntTest = newProblemTest[0]
        operatorTest = newProblemTest[1]
        secondIntTest = newProblemTest[2]
 
        if re.search('\D', firstIntTest) or re.search('\D', secondIntTest):
          return "Error: Numbers must only contain digits."
          inputTest = False
        if operatorTest != '+' and operatorTest != '-':
          return "Error: Operator must be '+' or '-'."
          inputTest = False
        if len(firstIntTest) > 4 or len(secondIntTest) > 4:
          return "Error: Numbers cannot be more than four digits."
          inputTest = False
      break

    # define string variables
    firstString = ''
    secondString = ''
    lineString = ''
    answerString = ''

    # sorts problems into strings
    if inputTest:
      for problem in problems:

          # define problem variables
          newProblem = problem.split()
          firstInt = newProblem[0]
          operator = newProblem[1]
          secondInt = newProblem[2]

          # find integer lengths
          firstIntLen = len(firstInt)
          secondIntLen = len(secondInt)
          dashLength = max(firstIntLen, secondIntLen) + 2

          # find firsString space
          firstStringSpace = dashLength - firstIntLen

          # find secondString space
          secondStringSpace = dashLength - secondIntLen - 1

          # assign string variables
          firstString += ' ' * firstStringSpace + firstInt + ' ' * 4
          secondString += operator + ' ' * secondStringSpace + secondInt + ' ' * 4
          lineString += '-' * dashLength + ' ' * 4

          # check for operator
          if newProblem[1] == '+':
              answer = int(firstInt) + int(secondInt)
          else:
              answer = int(firstInt) - int(secondInt)

          # solve for answer
          if solve:
              answerString += ' ' * (dashLength - len(str(answer))) + str(answer) + ' ' * 4

      # formats problem strings
      return (firstString.rstrip() + '\n' + secondString.rstrip() + '\n' + lineString.rstrip() + ('\n' if solve else '') + answerString.rstrip())