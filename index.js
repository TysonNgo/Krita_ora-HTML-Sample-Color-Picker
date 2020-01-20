/* in previous script: */
/*   define hsv_values */
/*   define key */

/* example:
hsv_values = {
  '41414': {h: 0, s: 0, v:100},
  ...
};
key = '41414';
*/

let CS = ColorSelector();
function HSVtoFeColorMatrixRGB(h, s, v) {
  /** modified this snippet:
   * https://stackoverflow.com/questions/17242144/javascript-convert-hsb-hsv-color-to-rgb-accurately#answer-17243070
   */
  let r, g, b, i, f, p, q, t;

  h = h/360;
  s = s/100;
  v = v/100;

  i = Math.floor(h * 6);
  f = h * 6 - i;
  p = v * (1 - s);
  q = v * (1 - f * s);
  t = v * (1 - (1 - f) * s);
  switch (i % 6) {
    case 0: r = v, g = t, b = p; break;
    case 1: r = q, g = v, b = p; break;
    case 2: r = p, g = v, b = t; break;
    case 3: r = p, g = q, b = v; break;
    case 4: r = t, g = p, b = v; break;
    case 5: r = v, g = p, b = q; break;
  }
  return {
    r: r,
    g: g,
    b: b
  };
};

for (let id in hsv_values){
  document.getElementById('button'+id).onclick = (function(id){
    return function(){
      document.getElementById('button'+key).classList.remove('selected');
      key = id;
      let hsv = hsv_values[id];
      this.classList.add('selected');
      CS.setHSV(hsv);
    };
  })(id);
}

CS.onchange = () => {
  let matrix = document.getElementById('colorMatrix'+key);
  let hsv = hsv_values[key];
  hsv.h = CS.h;
  hsv.s = CS.s;
  hsv.v = CS.v;
  let rgb = HSVtoFeColorMatrixRGB(CS.h, CS.s, CS.v);
  matrix.children[0].setAttribute('values', `0 0 0 0 ${rgb.r} 0 0 0 0 ${rgb.g} 0 0 0 0 ${rgb.b} 0 0 0 1 0`);

  let button = document.getElementById('button'+key);
  button.style.background = `rgb(${rgb.r*255},${rgb.g*255},${rgb.b*255})`;
};

CS.setHSV(hsv_values[key]);
document.getElementById('button'+key).classList.add('selected');