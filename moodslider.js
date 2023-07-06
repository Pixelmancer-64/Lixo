function(instance, properties, context) {
    
	const emoji = instance.canvas.get(0).querySelector('.emoji')
    const input = instance.canvas.get(0).querySelector('.rangeSlider');
    
    if(!instance.data.initialized){
        instance.data.value = properties.default_value
        input.value = instance.data.value
        
  		instance.publishState("value", instance.data.value);
  		input.style.setProperty("--range", `${instance.data.value}%`)
        

    }
    
    if(properties.floating_emoji_innerhtml){
        emoji.style.backgroundImage = ''
		emoji.innerHTML = properties.floating_emoji_innerhtml
    }
    
    if(properties.disabled){
        inputRange.disabled = true;
    	emoji.style.opacity = 0
    }
    
    emoji.style.backgroundImage = `url('${properties.emoji}')`
    
    
    input.style.setProperty("--emoji", `url('${properties.emoji}')`)
    input.style.setProperty("--progress", `${properties.progress_color}`)
    input.style.setProperty("--background", `${properties.background_color}`)
    

    
}