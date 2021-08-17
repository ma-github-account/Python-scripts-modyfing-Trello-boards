
from requests_and_json_management import *
import time

deleteAllBoards()

createABoard("Test3")
exampleBoardId = getExampleIdOfSomeExistingBoard()

createAList("TestList3", exampleBoardId)

#Making sure that above list creation rest request is processed before next request
#which creates card for that list is sent.
time.sleep(5)

createCardForAnyExistingList()

exampleOfExistingCardId = getAnExampleOfExistingCardId()
	
editCardsName(exampleOfExistingCardId, "CardTestName3")





