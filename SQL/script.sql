USE [master]
GO
/****** Object:  Database [Myries_Design_DB]    Script Date: 28/04/2022 15:37:12 ******/
CREATE DATABASE [Myries_Design_DB]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Myries_Design_DB', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Myries_Design_DB.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Myries_Design_DB_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Myries_Design_DB_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [Myries_Design_DB] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Myries_Design_DB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Myries_Design_DB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET ARITHABORT OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Myries_Design_DB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Myries_Design_DB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Myries_Design_DB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Myries_Design_DB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET RECOVERY FULL 
GO
ALTER DATABASE [Myries_Design_DB] SET  MULTI_USER 
GO
ALTER DATABASE [Myries_Design_DB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Myries_Design_DB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Myries_Design_DB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Myries_Design_DB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Myries_Design_DB] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Myries_Design_DB] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Myries_Design_DB', N'ON'
GO
ALTER DATABASE [Myries_Design_DB] SET QUERY_STORE = OFF
GO
USE [Myries_Design_DB]
GO
/****** Object:  Table [dbo].[Caracteristica]    Script Date: 28/04/2022 15:37:13 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Caracteristica](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_producto] [int] NULL,
	[nombre] [varchar](100) NULL,
	[tipo] [varchar](50) NULL,
	[precio] [bigint] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Producto]    Script Date: 28/04/2022 15:37:13 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Producto](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Caracteristica] ON 

INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (1, 1, N'20x20 cm', N'TAMANO', 23000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (2, 1, N'30x40 cm', N'TAMANO', 33000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (3, 1, N'40x50 cm', N'TAMANO', 43000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (4, 1, N'Persona Extra', N'EXTRAPERSONA', 5000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (5, 1, N'Mascota Extra', N'EXTRAMASCOTA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (6, 1, N'Montaje 2 fotos', N'MOTAJE', 2000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (7, 1, N'Liso', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (8, 1, N'Elaborado', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (9, 2, N'20x20 cm', N'TAMANO', 18000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (10, 2, N'30x40 cm', N'TAMANO', 28000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (11, 2, N'40x50 cm', N'TAMANO', 38000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (12, 2, N'Persona Extra', N'EXTRAPERSONA', 5000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (13, 2, N'Mascota Extra', N'EXTRAMASCOTA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (14, 2, N'Montaje 2 fotos', N'MOTAJE', 2000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (15, 2, N'Liso', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (16, 2, N'Elaborado', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (17, 3, N'20x20 cm', N'TAMANO', 15000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (18, 3, N'30x40 cm', N'TAMANO', 25000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (19, 3, N'40x50 cm', N'TAMANO', 35000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (20, 3, N'Persona Extra', N'EXTRAPERSONA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (21, 3, N'Mascota Extra', N'EXTRAMASCOTA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (22, 3, N'Montaje 2 fotos', N'MOTAJE', 2000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (23, 3, N'Liso', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (24, 3, N'Elaborado', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (25, 4, N'20x20 cm', N'TAMANO', 15000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (26, 4, N'30x40 cm', N'TAMANO', 25000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (27, 4, N'40x50 cm', N'TAMANO', 35000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (28, 4, N'Persona Extra', N'EXTRAPERSONA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (29, 4, N'Mascota Extra', N'EXTRAMASCOTA', 3000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (30, 4, N'Montaje 2 fotos', N'MOTAJE', 2000)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (31, 4, N'Liso', N'FONDO', 0)
INSERT [dbo].[Caracteristica] ([id], [id_producto], [nombre], [tipo], [precio]) VALUES (32, 4, N'Elaborado', N'FONDO', 0)
SET IDENTITY_INSERT [dbo].[Caracteristica] OFF
GO
SET IDENTITY_INSERT [dbo].[Producto] ON 

INSERT [dbo].[Producto] ([id], [nombre]) VALUES (1, N'Retrato Persona')
INSERT [dbo].[Producto] ([id], [nombre]) VALUES (2, N'Retrato Mascota')
INSERT [dbo].[Producto] ([id], [nombre]) VALUES (3, N'Ilustracion Persona')
INSERT [dbo].[Producto] ([id], [nombre]) VALUES (4, N'Ilustracion Mascota')
SET IDENTITY_INSERT [dbo].[Producto] OFF
GO
ALTER TABLE [dbo].[Caracteristica]  WITH CHECK ADD FOREIGN KEY([id_producto])
REFERENCES [dbo].[Producto] ([id])
GO
ALTER TABLE [dbo].[Caracteristica]  WITH CHECK ADD CHECK  (([tipo]='MOTAJE' OR [tipo]='FONDO' OR [tipo]='EXTRAMASCOTA' OR [tipo]='EXTRAPERSONA' OR [tipo]='TAMANO'))
GO
USE [master]
GO
ALTER DATABASE [Myries_Design_DB] SET  READ_WRITE 
GO
