$(document).ready(function() {
	var table = $('#apps').DataTable( {
		"lengthMenu": [[25, 50, -1], [25, 50, "All"]],
		order: [[2, "score"]],
		stateSave: true
		});
} );