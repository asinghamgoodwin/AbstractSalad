//get the box that was clicked on.
//remove is_hidden from that form
var clickEvents = function(){

	var categories = ["Greens","Veggies","Protein","Dressing","Other"];

	categories.forEach(function(cat){
		// document.getElementById("saladBlock" + cat).addEventListener('click', function(e){

		// 	var form = document.getElementById('saladForm' + cat).attributes['class'].value;

		// 	if(form === 'is_hidden')
		// 		document.getElementById('saladForm' + cat).attributes.removeNamedItem("class");
		// });



		$('#saladBlock'+cat).on('click', function(e){
			$('#saladForm'+cat).removeClass('is_hidden');

			
		});
		
	});
};


document.addEventListener('load', clickEvents());