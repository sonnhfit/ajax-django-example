function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function myfunc(){
    // alert(" xin chao");
    $.get( "/leadz/contact/", function( data ) {
        var datatable = '';
        data.forEach(element => {
            
            var tr = `
            <tr>
                <td>${element.title}</td>
                <td>${element.language}</td>
            </tr>
            `
            datatable += tr
           
        });
        $( "#mytb" ).html(datatable);
    });

}


function getRecommend(){
    
    console.log($("#se").val());

}