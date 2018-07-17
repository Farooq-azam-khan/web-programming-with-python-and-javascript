document.addEventListener('DOMContentLoaded', () => {
  // state 
  let draw = false; 
  
  // elements 
  let points = []; 
  let lines = []; 
  let svg = null; 
  
  function render() {
    // create selector area
    svg = d3.select('#draw')
            .attr('height', window.innerHeight)
            .attr('width', window.innerWidth); 
    
    // when mouse is clicked
    svg.on('mousedown', function () {
      draw = true; 
      const coords = d3.mouse(this); 
      draw_point(coords[0], coords[1], false); 
    }); // end of mousedown 
    
    // when mouse is released
    svg.on('mouseup', () => {
      draw = false; 
    }); // end of mouseup
    
    // mouse is moved
    svg.on('mousemove', function() {
      if(!draw){return;}
      const coords = d3.mouse(this); 
      draw_point(coords[0], coords[1], true); 
    }); // end of mousemove
    
    document.querySelector('#erase').onclick = () => {
      // console.log('points: ' + points);
      // console.log('points: ' + points);
      for (let i=0;i<points.length;i++){points[i].remove();}
      for (let i=0;i<lines.length;i++){lines[i].remove();}
      points = [];
      lines = [];
    } // endof erase selector
  } // end of render function 
  
  function draw_point(x, y, connect) {
    
    const color = document.querySelector('#color-picker').value; 
    const thickness = document.querySelector('#thickness-picker').value; 
    
    if (connect) {      
        const last_point = points[points.length-1]; 
        const line = svg.append('line')
                        .attr('x1', last_point.attr('cx'))
                        .attr('y1', last_point.attr('cy'))
                        .attr('x2', x)
                        .attr('y2', y)
                        .attr('stroke-width', thickness*2)
                        .style('stroke', color); 
        
        lines.push(line);      
    }
    
    const point = svg.append('circle')
                      .attr('cx', x)
                      .attr('cy', y)
                      .attr('r', thickness)
                      .style('fill', color);
    points.push(point);
  } // end of add_point function 
  render(); 
});