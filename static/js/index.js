layui.use(['carousel', 'form'], function(){
  var carousel = layui.carousel
  ,form = layui.form;
  //图片轮播
  carousel.render({
    elem: '#banner'
    ,width: '778px'
    ,height: '440px'
    ,interval: 5000
  });
});