'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import styles from './Sidebar.module.css'

type DocItem = { slug: string; title: string }
type ModuleItem = { id: string; title: string; docs: DocItem[] }

export default function SidebarNav({ modules, prefix }: { modules: ModuleItem[], prefix: string }) {
  const pathname = usePathname()

  return (
    <nav className={styles.sidebarNav}>
      {modules.map(mod => (
        <div key={mod.id} className={styles.moduleSection}>
          <h3 className={styles.moduleTitle}>{mod.title}</h3>
          <ul className={styles.docList}>
            {mod.docs.map(doc => {
              const href = `${prefix}/${mod.id}/${doc.slug}`
              const isActive = pathname === href
              return (
                <li key={doc.slug}>
                  <Link 
                    href={href} 
                    className={`${styles.docLink} ${isActive ? styles.active : ''}`}
                  >
                    {doc.title}
                  </Link>
                </li>
              )
            })}
          </ul>
        </div>
      ))}
    </nav>
  )
}
