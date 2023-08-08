{% include "header.tpl" %}
<script>
        function updateLabel(formObject){
             document.getElementById(formObject.id + 'Value').innerHTML = formObject.value
        }

        function updateAllFormValues(){
            Array.from(document.getElementById('updateForm').elements).forEach((input) => {
               updateLabel(input)
            });
        }

        function updateDome(){
            let updateRequest = new XMLHttpRequest();
            var red = parseInt(document.getElementById('color').value.substring(1, 3), 16);
            var green = parseInt(document.getElementById('color').value.substring(3, 5), 16);
            var blue = parseInt(document.getElementById('color').value.substring(5, 7), 16);
            updateRequest.open("GET", "https://192.168.0.127:5000/api/" + red + "/" + green + "/" + blue + "/" + document.getElementById('freq').value + "/" + document.getElementById('duty').value + "/" + document.getElementById('soundLength').value + "/" + document.getElementById('quietLength').value + "/" + document.getElementById('repeat').value);
            updateRequest.send();
        }

        window.onload = updateAllFormValues;
    </script>

<h2>Send Command to Dome</h2>
    <form id='updateForm' action='' method='post'>
    <table>
        <tr>
            <td class="leftColumn"><label for='color'>Color:</label></td>
            <td><input type='color' name='color' id='color' value='#FFFFFF'  onchange='updateLabel(this)'></td>
            <td><div id='colorValue' style="display: inline"></div></td>
        </tr>
        <tr>
            <td class="leftColumn"><label for='freq'>Frequency:</label></td>
            <td><input type='range' name='freq' id='freq' min='1000' max='4000000' onchange='updateLabel(this)'></td>
            <td><div id='freqValue' style="display: inline"></div> hz</td>
        </tr>
        <tr>
            <td class="leftColumn"><label for='duty'>Volume:</label></td>
            <td><input type='range' name='duty' id='duty' min='0' max='1023' onchange='updateLabel(this)'></td>
            <td><div id='dutyValue' style="display: inline"></div></td>
        </tr>
        <tr>
            <td class="leftColumn"><label for='soundLength'>Sound Length:</label></td>
            <td><input type='range' name='soundLength' id='soundLength' min='0' max='10' onchange='updateLabel(this)'></td>
            <td><div id='soundLengthValue' style="display: inline"></div> second(s)</td>
        </tr>
        <tr>
            <td class="leftColumn"><label for='quietLength'>Quiet Length:</label></td>
            <td><input type='range' name='quietLength' id='quietLength' min='0' max='10' onchange='updateLabel(this)'></td>
            <td><div id='quietLengthValue' style="display: inline"></div> second(s)</td>
        </tr>
        <tr>
            <td class="leftColumn"><label for='repeat'>Repeat:</label></td>
            <td><input type='range' name='repeat' id='repeat' min='0' max='10' onchange='updateLabel(this)'></td>
            <td><div id='repeatValue' style="display: inline"></div> time(s)</td>
        </tr>
        <tr>
            <td class="leftColumn"></td>
            <td><button type='button' onclick="updateDome()">Update</button></td>
        </tr>
    </table>
    </form>

{% include "footer.tpl" %}
