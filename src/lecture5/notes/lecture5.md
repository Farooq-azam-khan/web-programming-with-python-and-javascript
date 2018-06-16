# JavaScript
- having code run on client side takes the load off the server 
- faster because user does not need to communicate with client
- js is desgned with web-browsers. (es6 is latest.)
- in html file `<script> alert('hw'); </script>`

```JavaScript
function hello()
{
  alert('hello')
}
```
- events:
  - onclick
  - onmouseover
  - onkeydown
  - onkeyup
  - onload
  - onblur
- `document.querySelector('h1').innerHTML`
  - where it says `h1` it takes in a css selector, ie any html tag, id or class.  

## variables
- `const, let, var`
- `data-color`, or `data-arg` ...
  - this `data-` is used to add additional data to the html tag so that js can have more control over il
## arrow notation
- `() => { alert('hw')}`
  - es6's way of writing functions
  - eg `x => { x*2}`, if only one line `x => x*2`