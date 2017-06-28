var updateData = {};

function updateProjectData() {
	if (updateData.hasOwnProperty('id') && updateData.hasOwnProperty('status')) {
		updateData.csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
		$.post("/reflection/update/", updateData)
		.done(function (result) {
			if (result === "True") {
				alert("Successfully updated data.");
			} else if (result === "False") {
				alert("Failed to update data.");
			}
		});
	}
}

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