async function update_models(elem, selectid, currentModelId = 0, initInnerHTML = '', optionStartValue = 0, companyIndexOffset = 0) 
{
    let data = {
        idCompany: Number(elem.value) + 1 + companyIndexOffset,
    }

    let response = await fetch(`${window.origin}/update_models`, {
        cache: "no-cache",
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify(data)
    });

    let models = await response.json();

    let length = Object.keys(models['nameModelCar']).length;

    let select = document.getElementById(selectid);

    if (length == 0)
    {
        select.disabled = true;
    }
    else
    {
        select.disabled = false;
    }
    
    select.innerHTML = initInnerHTML;

    for (let i = optionStartValue; i < length + optionStartValue; i++)
    {
        let option = document.createElement("option");
        option.text = models["nameModelCar"][i - optionStartValue];
        option.value = i;

        if (models["idModelCar"][i - optionStartValue] == currentModelId)
        {
            option.selected = true;
        }

        select.appendChild(option);
    }
};