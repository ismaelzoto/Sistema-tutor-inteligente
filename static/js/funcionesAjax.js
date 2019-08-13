//window.onload = function () {
//    mostrarCursos();
//}

$(document).on("click", ".open-editarModal", function () {
    var Id = $(this).data('id');
    $(".modal-body #idcurso_m").val( Id );
    // As pointed out in comments,
    // it is superfluous to have to manually call the modal.
    $('#editarModal').modal('show');
});

function guardarCurso(){
    var ajaxRequest;
    var mensaje = document.getElementById("mensaje");

    if(window.XMLHttpRequest){
        ajaxRequest = new XMLHttpRequest();
    } else{
        ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var idCurso = document.getElementById("idcurso").value;
    var nombrecurso = document.getElementById("nombrecurso").value;
    var nivelcurso = document.getElementById("nivelcurso").value;

    var cadena = "idCurso=" + idCurso + "&nombreCurso=" + nombrecurso + "&nivelCurso=" + nivelcurso;

    ajaxRequest.onreadystatechange = function() {
        if (ajaxRequest.readyState === 4 && ajaxRequest.status === 200) {
            var resultado = ajaxRequest.responseText;
            mensaje.innerHTML = resultado;
        }
    };
    ajaxRequest.open("POST", "a_curso.jsp", true);
    ajaxRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    ajaxRequest.send(cadena);
    //mostrarCursos();
}

function editarCurso() {
    var ajaxRequest;
    var mensaje = document.getElementById("mensaje");

    if(window.XMLHttpRequest){
        ajaxRequest = new XMLHttpRequest();
    } else{
        ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var idCurso = document.getElementById("idcurso").value;
    var nombrecurso = document.getElementById("nombrecurso").value;
    var nivelcurso = document.getElementById("nivelcurso").value;

    var cadena = "idCurso=" + idCurso + "&nombreCurso=" + nombrecurso + "&nivelCurso=" + nivelcurso;

    ajaxRequest.onreadystatechange = function() {
        if (ajaxRequest.readyState === 4 && ajaxRequest.status === 200) {
            var resultado = ajaxRequest.responseText;
            mensaje.innerHTML = resultado;
        }
    };
    ajaxRequest.open("POST", "a_curso.jsp", true);
    ajaxRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    ajaxRequest.send(cadena);
}

function mostrarCursos() {
    $('#datos').load('m_cursos.jsp');
}