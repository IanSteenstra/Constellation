$(document).ready(function() {
	var table = $('#projects').DataTable( {
		"lengthMenu": [[25, 50, -1], [25, 50, "All"]],
		order: [[2, "date"]],
		stateSave: true
		});
} );