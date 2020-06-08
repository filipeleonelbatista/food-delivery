import React from 'react';
import { Item, Input, Icon, Label } from 'native-base';

class TextInputStyled extends React.Component{
    
    render(){
        const { label, icon, onChange } = this.props;
        return(
            <Item floatingLabel>
                <Label>{label}</Label>
                <Input onChangeText={(e) => { onChange(e)}} />
            </Item>
        );
    }
}

export default TextInputStyled;