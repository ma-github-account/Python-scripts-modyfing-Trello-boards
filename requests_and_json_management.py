
import json
import requests

trello_key="46a2a02d7bc21e39c34b247491fd679a"
trello_token="c53d4f3cb8ca161b58a7e8ba71c06d6e9982676907657560c2137acca89b490d"

def prepareGetRequest(get_request_specification):

    separator = '&' if '?' in get_request_specification else '?'
    request = f"https://api.trello.com/1/{get_request_specification}{separator}key={trello_key}&token={trello_token}"
    return request

def preparePostRequest(post_request_specification):

    separator = '&' if '?' in post_request_specification else '?'
    request = f"https://api.trello.com/1/{post_request_specification}{separator}key={trello_key}&token={trello_token}"
    return request

def prepareDeleteRequest(delete_request_specification):

    separator = '&' if '?' in delete_request_specification else '?'
    request = f"https://api.trello.com/1/{delete_request_specification}{separator}key={trello_key}&token={trello_token}"
    return request

def preparePutRequest(put_request_specification):

    separator = '&' if '?' in put_request_specification else '?'
    request = f"https://api.trello.com/1/{put_request_specification}{separator}key={trello_key}&token={trello_token}"
    return request

def getAllBoardsNames():

	get_response = requests.get(prepareGetRequest('members/me/boards?fields=name'))
	BoardsNamesDataInJsonFormat = json.loads(get_response.text)

	boards_names = []

	for i in range(len(BoardsNamesDataInJsonFormat)):
		Board = BoardsNamesDataInJsonFormat[i]
		boards_names.append(Board["name"])

	return boards_names

def getAllBoardsIds():

	get_response = requests.get(prepareGetRequest('members/me/boards?fields=id'))
	BoardsIdsDataInJsonFormat = json.loads(get_response.text)

	boards_ids = []

	for i in range(len(BoardsIdsDataInJsonFormat)):
		Board = BoardsIdsDataInJsonFormat[i]
		boards_ids.append(Board["id"])

	return boards_ids

def getExampleIdOfSomeExistingBoard():
	return getAllBoardsIds()[0]

def createABoard(name):

	post_request_specification = f"boards/?name={name}&defaultLists=false"
	post_request = requests.post(preparePostRequest(post_request_specification))

def deleteABoard(board_id):

	delete_request_specification = f"boards/{board_id}"
	delete_request = requests.delete(prepareDeleteRequest(delete_request_specification))

def deleteAllBoards():
	for board_id in getAllBoardsIds():
		deleteABoard(board_id)

def createAList(name, board_id):

	post_request_specification = f"lists?name={name}&idBoard={board_id}"
	post_request = requests.post(preparePostRequest(post_request_specification))

def createAListForAnyExistingBoard(name):

	exampleBoardId = getExampleIdOfSomeExistingBoard()
	createAList(name, exampleBoardId)

def getAllListsRelatedToGivenBoard(board_id):

	get_request_specification = f"boards/{board_id}/lists"
	get_response = requests.get(prepareGetRequest(get_request_specification))
	ListsIdsDataInJsonFormat = json.loads(get_response.text)

	lists_ids = []

	for i in range(len(ListsIdsDataInJsonFormat)):
		List = ListsIdsDataInJsonFormat[i]
		lists_ids.append(List["id"])

	return lists_ids

def createCardForGivenList(list_id):

	post_request_specification = f"cards?idList={list_id}"
	post_response = requests.post(prepareGetRequest(post_request_specification))

def getAllExistingListIds():

	ListOfExistingTrelloLists = []

	for board_id in getAllBoardsIds():
		for list_id in getAllListsRelatedToGivenBoard(board_id):
			ListOfExistingTrelloLists.append(list_id)

	return ListOfExistingTrelloLists

def getAnExampleOfExistingListId():
	return getAllExistingListIds()[0]

def createCardForAnyExistingList():

	exampleListId = getAnExampleOfExistingListId()
	createCardForGivenList(exampleListId)

def getAllCardsInAList(list_id):

	get_request_specification = f"lists/{list_id}/cards"
	get_response = requests.get(prepareGetRequest(get_request_specification))
	CardsIdsDataInJsonFormat = json.loads(get_response.text)

	cards_ids = []

	for i in range(len(CardsIdsDataInJsonFormat)):
		Card = CardsIdsDataInJsonFormat[i]
		cards_ids.append(Card["id"])

	return cards_ids

def getAllExistingCardIds():

	ListOfExistingTrelloCards = []

	for board_id in getAllBoardsIds():
		for list_id in getAllListsRelatedToGivenBoard(board_id):
			for card_id in getAllCardsInAList(list_id):
				ListOfExistingTrelloCards.append(card_id)

	return ListOfExistingTrelloCards

def getAnExampleOfExistingCardId():
	return getAllExistingCardIds()[0]

def deleteACard(card_id):

	delete_request_specification = f"cards/{card_id}"
	delete_request = requests.delete(prepareDeleteRequest(delete_request_specification))

def addACommentToACard(card_id, comment_text):

	post_request_specification = f"cards/{card_id}/actions/comments?text={comment_text}"
	post_response = requests.post(prepareGetRequest(post_request_specification))

def getNumberOfCommentsInCard(card_id):

	get_request_specification = f"cards/{card_id}"
	get_response = requests.get(prepareGetRequest(get_request_specification))
	BoardsNamesDataInJsonFormat = json.loads(get_response.text)

	return BoardsNamesDataInJsonFormat["badges"]["comments"]
	
def editCardsName(card_id, newName):

	put_request_specification = f"cards/{card_id}?name={newName}"
	put_response = requests.put(prepareGetRequest(put_request_specification))
	BoardsNamesDataInJsonFormat = json.loads(put_response.text)

def getCardsName(card_id):

	get_request_specification = f"cards/{card_id}"
	get_response = requests.get(prepareGetRequest(get_request_specification))
	BoardsNamesDataInJsonFormat = json.loads(get_response.text)

	return BoardsNamesDataInJsonFormat["name"]