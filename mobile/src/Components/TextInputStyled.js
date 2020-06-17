import React from 'react';
import { Item, Input, Icon, Label } from 'native-base';

class TextInputStyled extends React.Component{

    state = {
        isFocused: false
    };

    handleFocus = event =>{
        this.setState({ isFocused: true })
        if(this.props.onFocus){
            this.props.onFocus(event);
        }
    };
    handleBlur = event =>{
        this.setState({ isFocused: false })
        if(this.props.onBlur){
            this.props.onBlur(event);
        }
    };
    
    render(){
        const { isFocused } = this.state;
        const { label, icon, onChange } = this.props;

        return(
            <Item floatingLabel>
                <Label>{label}</Label>
                <Input 
                    selectionColor={ isFocused ? "#F00" : "#D3D3D3"} 
                    underlineColorAndroid={ isFocused ? "#F00" : "#D3D3D3"} 
                    onFocus={this.handleFocus}
                    onBlur={this.handleBlur}
                    onChangeText={(e) => { onChange(e)}} 
                     />
            </Item>
        );
    }
}

export default TextInputStyled;