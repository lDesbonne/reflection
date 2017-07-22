var updateData = {};

function updateProjectData() {
	if (updateData.hasOwnProperty('id') && updateData.hasOwnProperty('status')) {
		updateData.csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
		$.post("/reflection/update/", updateData)
		.done(function (result) {
			if (result === "True") {
				alert("Successfully updated data.");
				location.reload();
			} else if (result === "False") {
				alert("Failed to update data.");
				location.reload();
			}
		});
	}
}

function removePendingStudies() {
	for (var i = 0; i < pendingStudies.length; i++) {
		var researchId = pendingStudies[i];
		if (document.getElementById(researchId)) {
			document.getElementById(researchId).setAttribute("class", "collapse");
		}
	}
}