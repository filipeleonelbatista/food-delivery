import React, { BackHandler } from 'react';
import { StyleSheet, View, Alert } from 'react-native';
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
    <View style={{ flex: 1 }}>
      <DrawerContentScrollView {...props}>
        <View style={styles.drawerContent}>
          <View style={styles.userInfoSection}>
            <View style={{ flexDirection: 'row', marginTop: 15 }}>
              <Avatar.Image
                source={AvatarDefault}
                size={50}
              />
              <View style={{ marginLeft: 15, flexDirection: 'column' }}>
                <Title style={styles.title}>Administrador</Title>
                <Caption style={styles.caption}>Adm. do sistema</Caption>
              </View>
            </View>

            <View style={styles.row}>
              <View style={styles.section}>
                <Paragraph style={[styles.paragraph, styles.caption]}>80</Paragraph>
                <Caption style={styles.caption}>Pendentes</Caption>
              </View>
              <View style={styles.section}>
                <Paragraph style={[styles.paragraph, styles.caption]}>100</Paragraph>
                <Caption style={styles.caption}>Em prdução</Caption>
              </View>
            </View>
          </View>

          <Drawer.Section style={styles.drawerSection}>
            <DrawerItem
              icon={({ color, size }) => (
                <Icon
                  name="account-badge-outline"
                  color={color}
                  size={size}
                />
              )}
              label="Perfil"
              onPress={() => { }}
            />
          </Drawer.Section>

          <Drawer.Section style={styles.drawerSection}>
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
          </Drawer.Section>
          <Drawer.Section style={styles.drawerSection}>
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
          </Drawer.Section>

          <Drawer.Section style={styles.drawerSection}>
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

          {/* <Drawer.Section title="Preferences">
                        <TouchableRipple onPress={() => {toggleTheme()}}>
                            <View style={styles.preference}>
                                <Text>Dark Theme</Text>
                                <View pointerEvents="none">
                                    <Switch value={paperTheme.dark}/>
                                </View>
                            </View>
                        </TouchableRipple>
                    </Drawer.Section> */}
        </View>
      </DrawerContentScrollView>
      <Drawer.Section style={styles.bottomDrawerSection}>
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
  drawerContent: {
    flex: 1,
  },
  userInfoSection: {
    paddingLeft: 20,
  },
  title: {
    fontSize: 16,
    marginTop: 3,
    fontWeight: 'bold',
  },
  caption: {
    fontSize: 14,
    lineHeight: 14,
  },
  row: {
    marginTop: 20,
    flexDirection: 'row',
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
  },
  bottomDrawerSection: {
    marginBottom: 15,
    borderTopColor: '#f4f4f4',
    borderTopWidth: 1
  },
  preference: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
});