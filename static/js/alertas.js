
function file_ok(){
    swal({
            title: "Registrado",
            text: "El archivo ha sido guardado en la base de datos.",
            timer: 4000,
            type: "success"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function file_error(){
    swal({
            title: "Error",
            text: "El archivo no ha sido guardado en la base de datos. S\u00F3lo acepta archivos con extensi\u00F3n .txt. Favor de revisar la extensi\u00F3n e intente subirlo otra vez.",
            type: "error"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function text_ok(){
    swal({
            title: "Registrado",
            text: "El texto ha sido guardado en la base de datos.",
            timer: 4000,
            type: "success"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function text_error(){
    swal({
            title: "Error",
            text: "El texto no ha sido guardado en la base de datos. Favor de revisar el texto y volver a intentarlo.",
            type: "error"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function analisis_text_ok(){
    swal({
            title: "Registrado",
            text: "El texto ha sido analizado correctamente.",
            timer: 4000,
            type: "success"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function analisis_text_error(){
    swal({
            title: "Error",
            text: "El texto no ha sido analizado.",
            type: "error"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function text_error_vacio(){
    swal({
            title: "Error",
            text: "Debe introducir texto. Favor de capturar un texto y volver a intentarlo.",
            type: "error"
        },
        function(){
            //event to perform on click of ok button of sweetalert
        });
}
function borrar_documento(id_to_delete) {
    var confirmation = confirm('\u00BFEst\u00E1 seguro de que desea eliminar el texto? ');

    if(confirmation)
    {
        window.location = "borrar_documento.jsp?id="+id_to_delete;
    }
}
function abrirVentana(documento){
    window.open("/admin/resultados-doc.jsp?id="+documento, "Resultados", "status=1,width=860,height=550");
}
function abrirPdf(documento){
    window.open("/admin/reporte-pdf.jsp?id="+documento, "Resultados", "status=1,width=860,height=550");
}
function abrirPdf2(documento){
    window.open("/reporte-pdf.jsp?id="+documento, "Resultados", "status=1,width=860,height=550");
}
function verif(formu) {
    if (formu.password.value==formu.password_again.value) {
        return true
    } else {
        errorPassword(); return false
    }
}