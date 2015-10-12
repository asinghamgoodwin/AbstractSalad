//get the box that was clicked on.
//remove is_hidden from that form
var clickEvents = function(){

	var categories = ["Greens","Veggies","Protein","Dressing","Other"];

	var prev;

	categories.forEach(function(cat){
		// document.getElementById("saladBlock" + cat).addEventListener('click', function(e){

		// 	var form = document.getElementById('saladForm' + cat).attributes['class'].value;

		// 	if(form === 'is_hidden')
		// 		document.getElementById('saladForm' + cat).attributes.removeNamedItem("class");
		// });
		

		$(document).on('click','#saladBlock' + cat, function(e){

			e.stopPropagation();

			if (prev) {
				prev.addClass('is_hidden');
				console.log(prev);
			}
			var len = this.childNodes.length;
			console.log(this.childNodes[len - 2]);
			$('#saladForm' + cat).removeClass('is_hidden');
			prev = $("#saladForm" +cat);

		});

		$(document).on('click', function(e){
			$('#saladForm' + cat).addClass('is_hidden');
		});


	});
};


document.addEventListener('load', clickEvents());