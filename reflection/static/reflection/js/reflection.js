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