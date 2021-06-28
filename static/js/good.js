$("#subject").on('change',function(){
    if($(this).find('option:selected').text()=="ระบบแรงดัน")
        $("#btn_submit").attr('disabled',true)
    else
        $("#btn_submit").attr('disabled',false)
}).trigger("change");





$("#topic").on('change',function(){
    if($(this).find('option:selected').text()=="ระบบแรงดัน")
        $("#btn_submit").attr('disabled',true)
    else
        $("#btn_submit").attr('disabled',false)
}).trigger("change");