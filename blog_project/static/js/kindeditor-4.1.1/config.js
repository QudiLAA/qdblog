/**
 * Created by Python on 2017/6/27.
 */
KindEditor.ready(function(K){
    K.create('textarea[name=content]',{
        width: '500',
        height: '200',
        uploadJson: '/admin/upload/kindeditor',
    });

});