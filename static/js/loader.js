$(document).ready(function(){
		$('a').click(function(e){
			e.preventDefault();
			$("#test").load($(this).attr('href'));
		});
	});




/*$(document).ready(function(){
	$("#test").load("../about.html");
});
$(document).ready(function(){
	$("#test").load("../index.html");
});
$(document).ready(function(){
	$("#test").load("../classes.html");
});
$(document).ready(function(){
	$("#test").load("../FQA.html");
});

$('a').click(function(){
		var page = (this).attr('href');
		$("#test").load(page);
		
		return false;
});*/