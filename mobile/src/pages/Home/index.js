import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function Home({route, navigation}) {
    return (
        <View style={styles.container}>
            <Text>Seu email: {route.params.email} </Text>
            <Text>Sua senha: {route.params.password} </Text>
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
