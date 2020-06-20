import React, { BackHandler } from 'react';
import { StyleSheet, View, Alert, ImageBackground } from 'react-native';

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
            <Avatar.Image
              source={AvatarDefault}
              size={64}
              style={{
                alignItems: 'center',
                justifyContent: 'center',
              }}
            />
          </TouchableOpacity>
          <View style={{ marginLeft: 15, flexDirection: 'column' }}>
            <Title style={styles.title}>Administrador</Title>
            <Caption style={styles.caption}>Adm. do sistema</Caption>
          </View>
        </View>
        <View style={{flexDirection:'column', marginTop:16}}>
          <Paragraph style={[styles.paragraph, styles.caption]}>Ganhos</Paragraph>
          <View style={{flexDirection:'row', marginTop:8, alignItems:'center'}}>
            <View style={{ flex: 1, flexDirection:'column', alignItems:'center' }}>
              <Paragraph style={[styles.paragraph, styles.caption]}>R$ 80,00 </Paragraph>
              <Caption style={styles.caption}>Diário</Caption>
            </View>
            <View style={{ flex: 1, flexDirection:'column', alignItems:'center' }}>
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
                  name="view-dashboard-outline"
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
                <Icon
                  name="file-document-outline"
                  color={color}
                  size={size}
                />
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
              label="Produtos"
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
});