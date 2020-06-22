import React, { BackHandler } from 'react';
import { StyleSheet, View, Alert, Image } from 'react-native';

import { TouchableOpacity } from 'react-native-gesture-handler';

import {
  useTheme,
  Avatar,
  Title,
  Caption,
  Paragraph,
  Drawer,
  Text,
  TouchableRipple,
  Switch
} from 'react-native-paper';
import {
  DrawerContentScrollView,
  DrawerItem
} from '@react-navigation/drawer';

import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

import Toast from 'react-native-tiny-toast'

import AvatarDefault from '../Assets/avatar-default.jpg'

export default function DrawerContent(props) {
  const paperTheme = useTheme();
  function handleExit() {
    Alert.alert(
      "Sair da aplicação",
      "Deseja realmente sair da aplicação?",
      [
        {
          text: "Sim", onPress: () => {

            Toast.show('Saindo da aplicação')
            props.navigation.navigate('Login')
          }
        },
        {
          text: "Não", onPress: () => {
            props.navigation.closeDrawer();
          }
        }
      ],
      { cancelable: false }
    );
  }
  return (
    <View style={{ flex: 1, backgroundColor: "#FFF" }}>
      <View style={styles.userInfoSection}>
        <View style={{ flexDirection: 'row', marginTop: 15 }}>
          <TouchableOpacity
            onPress={() => { }}
            activeOpacity={0.6}
            style={styles.item}
          >
            <Image
              source={AvatarDefault}
              style={{
                height: 64,
                width: 64,
                borderRadius: 32,
              }}
            />
          </TouchableOpacity>
          <View style={{ marginLeft: 15, flexDirection: 'column' }}>
            <Title style={styles.title}>Administrador</Title>
            <Caption style={styles.caption}>Adm. do sistema</Caption>
          </View>
        </View>
        <View style={{ flexDirection: 'column', marginTop: 16 }}>
          <View style={{ flexDirection: 'row', marginTop: 8, alignItems: 'center' }}>
            <View style={{ flex: 1, flexDirection: 'column', alignItems: 'center' }}>
              <Paragraph style={[styles.paragraph, styles.caption]}>R$ 80,00 </Paragraph>
              <Caption style={styles.caption}>Diário</Caption>
            </View>
            <View style={{ flex: 1, flexDirection: 'column', alignItems: 'center' }}>
              <Paragraph style={[styles.paragraph, styles.caption, { flex: 1 }]}>R$ 180,00 </Paragraph>
              <Caption style={styles.caption}>Mensal</Caption>
            </View>
          </View>
        </View>
      </View>
      <DrawerContentScrollView {...props} >
        <View style={styles.bottomDrawerSection}>
          <Drawer.Section style={styles.bottomDrawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="home"
                  color={color}
                  size={size}
                />
              )}
              label="Página inicial"
              onPress={() => { props.navigation.navigate('Home') }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="wallet-outline"
                  color={color}
                  size={size}
                />
              )}
              label="Vendas"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="account-group"
                  color={color}
                  size={size}
                />
              )}
              label="Clientes"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <>
                <View style={styles.notification}>
                  <Text style={styles.notificationText}>1</Text>
                </View>
                <Icon
                  name="file-document-outline"
                  color={color}
                  size={size}
                />
                </>
              )}
              label="Pedidos"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="inbox-multiple"
                  color={color}
                  size={size}
                />
              )}
              label="Cardápio"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="truck-delivery"
                  color={color}
                  size={size}
                />
              )}
              label="Entregas"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="food"
                  color={color}
                  size={size}
                />
              )}
              label="Cosinha"
              onPress={() => { }}
            />
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="account-group-outline"
                  color={color}
                  size={size}
                />
              )}
              label="Usuários"
              onPress={() => { }}
            />
          </Drawer.Section>
        </View>
      </DrawerContentScrollView>
      <Drawer.Section style={styles.bottomDrawerSection} >
        <DrawerItem
          icon={({ color, size }) => (
            <Icon
              name="logout"
              color={color}
              size={size}
            />
          )}
          label="Sair"
          onPress={() => { handleExit() }}
        />
      </Drawer.Section>
    </View>
  );
}

const styles = StyleSheet.create({
  item: {
    backgroundColor: '#fff',
    height: 64,
    width: 64,
    borderRadius: 32,
    marginRight: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  drawerContent: {
    flex: 1,
  },
  userInfoSection: {
    paddingLeft: 20,
    paddingBottom: 20,
    backgroundColor: '#E20030'
  },
  title: {
    fontSize: 16,
    marginTop: 3,
    fontWeight: 'bold',
    color: "#FFF"
  },
  caption: {
    fontSize: 14,
    lineHeight: 14,
    color: "#FFF"
  },
  row: {
    marginTop: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  column: {
    marginTop: 20,
    flexDirection: 'column',
    alignItems: 'center',
  },
  section: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 15,
  },
  paragraph: {
    fontWeight: 'bold',
    marginRight: 3,
  },
  drawerSection: {
    marginTop: 15,
    backgroundColor: "#FFF"
  },
  bottomDrawerSection: {
    marginBottom: 15,
    borderTopColor: '#FFF',
    borderTopWidth: 1
  },
  preference: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
  notification:{
    position:'absolute',
    top: 8,
    left: 20,
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor:"#F00",
    shadowColor: "#FFF",
    shadowOffset: {
        width: 0,
        height: 3,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,

    elevation: 6,
    alignItems:'center',
    justifyContent: 'center',
},
notificationText:{
    color:"#FFF",
    fontSize:10,
},
});