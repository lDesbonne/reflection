function submitProposal(){
	var hypothesis = "";
	var title = "";
	var details = "";
	var email = "";
	
	var proposal = {
			"hypothesis":hypothesis,
			"title":title,
			"detail":details,
			"email":email
	}
	
	var request = new XMLHttpRequest();
	
	request.open("POST",
			"/proposal");
	request.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
	request.send(proposal);
}