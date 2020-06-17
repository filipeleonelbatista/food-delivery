import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function Home({route, navigation}) {
    let email = route.params.email;
    let password = route.params.password;

    return (
        <View style={styles.container}>
            <Text>Seu email: {email} </Text>
            <Text>Sua senha: {password} </Text>
        </View>

    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});
