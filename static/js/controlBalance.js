

var px1= document.getElementById('p1');
var px2= document.getElementById('p2');
var px3= document.getElementById('p3');
var px4= document.getElementById('p4');
var px5= document.getElementById('p5');
var px6= document.getElementById('p6');
var px7= document.getElementById('p7');
var px8= document.getElementById('p8');
var px9= document.getElementById('p9');
var px10= document.getElementById('p10');
var px11= document.getElementById('p11');
var px12= document.getElementById('p12');
var px13= document.getElementById('p13');
var px14= document.getElementById('p14');
var px15= document.getElementById('p15');
var px16= document.getElementById('p16');
var px17= document.getElementById('p17');
var px18= document.getElementById('p18');
var px19= document.getElementById('p19');
var px20= document.getElementById('p20');
var px21= document.getElementById('p21');

function ocultarTodo(){
    document.getElementById('p1').classList.remove('dflex');
    document.getElementById('p1').classList.add('esconder');
    document.getElementById('p2').classList.remove('dflex');
    document.getElementById('p2').classList.add('esconder');
    document.getElementById('p3').classList.remove('dflex');
    document.getElementById('p3').classList.add('esconder');
    document.getElementById('p4').classList.remove('dflex');
    document.getElementById('p4').classList.add('esconder');
    document.getElementById('p5').classList.remove('dflex');
    document.getElementById('p5').classList.add('esconder');
    document.getElementById('p6').classList.remove('dflex');
    document.getElementById('p6').classList.add('esconder');
    document.getElementById('p7').classList.remove('dflex');
    document.getElementById('p7').classList.add('esconder');
    document.getElementById('p8').classList.remove('dflex');
    document.getElementById('p8').classList.add('esconder');
    document.getElementById('p9').classList.remove('dflex');
    document.getElementById('p9').classList.add('esconder');
    document.getElementById('p10').classList.remove('dflex');
    document.getElementById('p10').classList.add('esconder');
    document.getElementById('p11').classList.remove('dflex');
    document.getElementById('p11').classList.add('esconder');
    document.getElementById('p12').classList.remove('dflex');
    document.getElementById('p12').classList.add('esconder');
    document.getElementById('p13').classList.remove('dflex');
    document.getElementById('p13').classList.add('esconder');
    document.getElementById('p14').classList.remove('dflex');
    document.getElementById('p14').classList.add('esconder');
    document.getElementById('p15').classList.remove('dflex');
    document.getElementById('p15').classList.add('esconder');
    document.getElementById('p16').classList.remove('dflex');
    document.getElementById('p16').classList.add('esconder');
    document.getElementById('p17').classList.remove('dflex');
    document.getElementById('p17').classList.add('esconder');
    document.getElementById('p18').classList.remove('dflex');
    document.getElementById('p18').classList.add('esconder');
    document.getElementById('p19').classList.remove('dflex');
    document.getElementById('p19').classList.add('esconder');
    document.getElementById('p20').classList.remove('dflex');
    document.getElementById('p20').classList.add('esconder');
    document.getElementById('p21').classList.remove('dflex');
    document.getElementById('p21').classList.add('esconder');
}
/**
 * rango de los campos a rellenar TOTAL 21
 * @param {inicio del rango de campos} inicio 
 * @param {* fin del rango de campos} fin 
 */
function mostrarConRango(inicio, fin){
    ocultarTodo();
    for( var a=inicio;a<=fin;a++){
        document.getElementById('p'+String(a)).classList.add('dflex');
        document.getElementById('p'+String(a)).classList.remove('esconder');
    }
    document.getElementById('btnGuardarBalance').classList.remove('dflex');
    document.getElementById('btnGuardarBalance').classList.add('esconder');
}
/* mostrar el paso final 
    ya que debe mostrar el boton de guardar*/
function pasoFinal(){
    ocultarTodo();
    mostrarConRango(19,21);
    document.getElementById('btnGuardarBalance').classList.add('dflex');
    document.getElementById('btnGuardarBalance').classList.remove('esconder');
}

/* para marcar la barra lateral el paso que en el que se esta*/
function mostrarPaso(paso){
    for(var a=1;a<=6;a++){
        if(a!=paso){
            document.getElementById('pasoB'+String(a)).classList.add('fondoNegro');
            document.getElementById('pasoB'+String(a)).classList.remove('fondoSeleccion');
        }else{
            document.getElementById('pasoB'+String(a)).classList.remove('fondoNegro');
            document.getElementById('pasoB'+String(a)).classList.add('fondoSeleccion');
        }
    }
}

// inicialmente mostramos el paso1
mostrarConRango(1,5),
mostrarPaso(1)
