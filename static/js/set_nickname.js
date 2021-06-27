var token = $('input[name=csrfmiddlewaretoken]').val();

// ajax請求改昵稱
$('#id_edit').click(function() {
    $.ajax({
        url:'/blog/set_nickname/',
        type:'post',
        data:{
            'new_nickname':$('#id_new_nickname').val(),
            csrfmiddlewaretoken: token,
        },
        success:function (args) {
            if (args.code == 2000) {
                swal({
                    title: "",
                    text: args.msg,
                    type: "success",
                },
                function(){
                    window.location.reload()
                });
            }else{
                swal(args.msg,'','warning')
            }
        }
    })
})