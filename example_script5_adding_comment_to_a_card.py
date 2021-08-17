
from requests_and_json_management import *
import time

deleteAllBoards()

createABoard("Test5")

exampleBoardId = getExampleIdOfSomeExistingBoard()

createAList("TestList5", exampleBoardId)

#Making sure that above list creation rest request is processed before next request
#which creates card for that list is sent.
time.sleep(5)

for i in range(3):
	createCardForAnyExistingList()

exampleIdOfCardThatTheCommentWillBeAddedTo = getAnExampleOfExistingCardId()

addACommentToACard(exampleIdOfCardThatTheCommentWillBeAddedTo, "TestCommentText1")





