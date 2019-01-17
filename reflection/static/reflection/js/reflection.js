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

//Code snippets
//Enter and exit
//Add extra nodes to a selection to accomodate more data
//d3.select("body")
//.selectAll("p")
//.data([4, 8, 15, 16, 23, 42])
//.enter().append("p")
//  .text(function(d) { return "I’m number " + d + "!"; });

//Split the enter and exit operation into 3 parts for better control
//Update…
//var p = d3.select("body")
//  .selectAll("p")
//  .data([4, 8, 15, 16, 23, 42])
//    .text(function(d) { return d; });

// Enter…
//p.enter().append("p")
//    .text(function(d) { return d; });

// Exit…
//p.exit().remove();

//Transitions
//To fade the background to black
//d3.select("body").transition()
//.style("background-color", "black");
//Resize circles with a staggered delay
//d3.selectAll("circle").transition()
//.duration(750)
//.delay(function(d, i) { return i * 10; })
//.attr("r", function(d) { return Math.sqrt(d * scale); });
//The term d is used to refer to bound data