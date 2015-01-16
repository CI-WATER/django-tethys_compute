
function add_listeners(elem){
    var update_elem = elem;
    var id = elem.getAttribute('for');
    var ref_elem = document.getElementById(id);
    function update(){
        update_elem.value = ref_elem.value;
    }
    ref_elem.addEventListener('mousedown', function(){
        this.addEventListener('mousemove', update);
    });
    ref_elem.addEventListener('mouseup', function(){
        this.removeEventListener('mousemove', update)
        update();
    });
}

add_listeners(document.getElementById('size_output'));


for(var i=start_index, len=start_index + num_clusters;i<len;i++){
    var output_id = 'size_output_' + i;
    add_listeners(document.getElementById(output_id));
}