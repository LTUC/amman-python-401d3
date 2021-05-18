## Notes

### User Stories focus is on the User's interaction and experience


We cannot capture every detail in the User Stories sentence alone


### Acceptance Criteria - List of criteria a feature need to meet to be considered 'correct'

May include samples of input and output or it may just describe classes of input / output

Usually include edge cases and a definition of what the expected way to handle the edge case is

Example for Cheating / Typo Detection Feature

- Fails validation if a user enters number than is not on the list of rolls
- Fails validation if a user enters more numbers than are available on the list of rolls
- Passes validation if a user enters more numbers that are a subset of the dies in the roll

#### Subset:
Let A = (1,1,2,3,4, 5)
Let B = (2, 3)

B is a subset of A

Let C = (1,2,3,4)

C is a subset of A
Let D = (5,5)
D is not a subset of A

#### Assumptions:

In Software Development we often have to make assumptions. This is not a problem or a bad thing; we simply need to be aware of and sometimes explicitly state our assumptions. As you work through the stages of developing your software be mindful of what assumptions we are making. Sometimes you may need to prove it out to continue in other cases you cannot continue without making an assumption.

Product Owner -> Dev = Build code that can pass these tests
Product Owner -> Quality Assurance = run these tests on the program and check that they pass 
(can be manual or automated)

Who writes tests usually?

- Senior Dev
- Dev working on a feature esp. when NFR that new features include a minimum test coverage

Test Coverage -

```python
if a == 1:
    print('yes')
else:
    print('no')
```

Two cases / branches

With test coverage we are measuring what percentage of the overall code and branches are executed or 'covered' by tests i.e. some test is written that causes that code in a specific branch to run.

TDD - Q. How can a developer wrote tests for code that doesn't exist?

It depends on the Acceptance Criteria.

When you convert your UAT to test code in the case of unit tests you HAVE to make assumptions or decisions about the shape of the code. e.g. 
The following code assumes three things
1. In the present working directory we have a package called game_of_greed
2. In the game_of_greed package we have a module called game_logic
3. In the game_logic module we have defined 'Game'

```
from game_of_greed.game_logic import Game
```

A ticket may have: -
User Story
Description
Acceptance Criteria
Non Functional Requirements - Do not affect the functionality of the code i.e. test coverage must be above 80%
Screenshots

Behaviour Driven Development - Gherkin format

Can be used for describe User Acceptance Tests

Given that the user made a roll
When the user enters a list of keeps
Then validate that the keepers is a subset of the roll
